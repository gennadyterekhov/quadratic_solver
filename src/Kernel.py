import cmath


class Kernel:
    VALID_PARAMETERS_LENGTH = 4
    DEFAULT_ACTION = 'solve'

    def __init__(self, argv):
        self.cli_parameters = argv
        self.coefficients = [None] * (self.VALID_PARAMETERS_LENGTH - 1)
        self.action = self.DEFAULT_ACTION
        self.validate_parameters()
        self.set_action_from_parameters()
        self.perform()

    def validate_parameters(self):
        self.validate_parameters_length()
        self.validate_parameters_type()

    def validate_parameters_type(self):
        try:
            self.coefficients = list(
                map(float, self.cli_parameters[1:self.VALID_PARAMETERS_LENGTH])
            )
        except Exception as exception:
            raise Exception(
                f'Some of the parameters is not a number\n{exception}'
            )

    def validate_parameters_length(self):
        if len(self.cli_parameters) < self.VALID_PARAMETERS_LENGTH:
            raise Exception(
                f'Wrong number of parameters. You must supply {self.VALID_PARAMETERS_LENGTH - 1} parameters'
            )

    def set_action_from_parameters(self):
        if len(self.cli_parameters) > self.VALID_PARAMETERS_LENGTH:
            self.action = self.cli_parameters[self.VALID_PARAMETERS_LENGTH]

    def perform(self):
        try:
            default_method = getattr(self, self.DEFAULT_ACTION)
            method = getattr(self, self.action, default_method)
        except Exception as exception:
            raise Exception(f'Chosen action is not available.\n{exception}')
        return method()

    def solve(self):
        a, b, c = self.coefficients
        roots = [
            (-b + cmath.sqrt(b**2 - 4 * a * c)) / float(2 * a),
            (-b - cmath.sqrt(b**2 - 4 * a * c)) / float(2 * a)
        ]
        return roots
