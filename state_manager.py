class StateManager:
    def __init__(self, actual, new):
        self.actual = actual
        self.new = new

    @staticmethod
    def get_id(value: dict) -> str:
        return value.get('id')

    def is_diff(self) -> bool:
        """
        check bool, if var state_actual != var state_new
        :return:
        """
        check = self.get_id(self.actual) != self.get_id(self.new)
        return check

    def set_next_state(self):
        self.actual = self.new
        self.new = {}
