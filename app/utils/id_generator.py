import threading
import time


class IdGenerator:
    """
    Snowflake-style ID Generator

    64-bit Layout:
    -------------------------------------------------------
    | 41 bits Timestamp | 10 bits Machine ID | 12 bits Seq |
    -------------------------------------------------------
    """

    def __init__(self, machine_id: int):
        # Custom epoch (Jan 1, 2025 UTC in milliseconds)
        self.EPOCH = 1735689600000

        # Bit allocation
        self.machine_bits = 10
        self.sequence_bits = 12

        # Maximum values
        self.max_machine_id = (1 << self.machine_bits) - 1
        self.max_sequence = (1 << self.sequence_bits) - 1

        # Shift values
        self.machine_shift = self.sequence_bits
        self.timestamp_shift = self.machine_bits + self.sequence_bits

        # Validate machine ID
        if machine_id < 0 or machine_id > self.max_machine_id:
            raise ValueError(
                f"Machine ID must be between 0 and {self.max_machine_id}"
            )

        # Runtime state
        self.machine_id = machine_id
        self.sequence = 0
        self.last_timestamp = -1

        # Thread safety
        self.lock = threading.Lock()

    def _current_timestamp(self) -> int:
        """
        Returns milliseconds since custom epoch.
        """
        return int(time.time() * 1000) - self.EPOCH

    def _wait_next_millis(self, last_timestamp: int) -> int:
        """
        Wait until the next millisecond.
        """
        timestamp = self._current_timestamp()

        while timestamp <= last_timestamp:
            timestamp = self._current_timestamp()

        return timestamp

    def next_id(self) -> int:
        """
        Generate the next unique Snowflake ID.
        """
        with self.lock:
            timestamp = self._current_timestamp()

            # Clock moved backwards
            if timestamp < self.last_timestamp:
                raise Exception("Clock moved backwards. Refusing to generate ID.")

            # Same millisecond
            if timestamp == self.last_timestamp:

                self.sequence = (self.sequence + 1) & self.max_sequence

                # Sequence overflow
                if self.sequence == 0:
                    timestamp = self._wait_next_millis(self.last_timestamp)

            else:
                # New millisecond
                self.sequence = 0

            self.last_timestamp = timestamp

            snowflake_id = (
                (timestamp << self.timestamp_shift)
                | (self.machine_id << self.machine_shift)
                | self.sequence
            )

            return snowflake_id

id_generator = IdGenerator(machine_id=1)