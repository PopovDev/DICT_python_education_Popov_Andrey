"""Super credit calculator."""


from argparse import ArgumentParser
import math


class SuperCreditCalc:
    """Class for super credit calculator."""

    def __init__(self) -> None:
        """Initialize class."""
        self.parser = ArgumentParser(
            description="Credit calculator by Popov Andrey", conflict_handler="resolve")
        self.parser.add_argument("--type", choices=["annuity", "diff"],
                                 required=True, help="type of payment (annuity or diff)",
                                 type=str)
        self.parser.add_argument(
            "--payment", help="monthly payment", type=float)
        self.parser.add_argument(
            "--principal", help="loan principal", type=float)
        self.parser.add_argument(
            "--periods", help="number of months", type=int)
        self.parser.add_argument("--interest", help="interest rate",
                                 type=float, required=True)
        self.args = self.parser.parse_args()
        self.percent_interest = self.args.interest / 100
        self.principal = self.args.principal
        self.periods = self.args.periods
        self.payment = self.args.payment
        self.type = self.args.type

    @staticmethod
    def calculate_differentiated_payments(periods: int, principal: float, interest: float) -> None:
        """Calculate differentiated payments.

        Parameters:
        - periods: number of months during which the loan will be repaid
        - principal: initial principal of the loan
        - interest: interest rate on a loan, expressed as a decimal fraction
        """

        overpayment = 0
        monthly_interest_rate = interest / 12
        monthly_principal = principal / periods

        for period in range(periods):
            unpaid_principal = principal - monthly_principal * period
            interest_current = monthly_interest_rate * unpaid_principal
            monthly_payment = math.ceil(monthly_principal + interest_current)
            overpayment += monthly_payment
            print(f"Month {period + 1}: payment is {monthly_payment}")

        print(f"Overpayment: {math.ceil(overpayment - principal)}")

    @staticmethod
    def calculate_annuity_payment(periods: int, principal: float, interest: float) -> None:
        """Calculate the annuity payment.

        Parameters:
        - periods: number of months during which the loan will be repaid
        - principal: initial principal of the loan
        - interest: interest rate on a loan, expressed as a decimal fraction
        """

        monthly_interest_rate = interest / 12
        annuity_payment = principal * (
            monthly_interest_rate * (1 + monthly_interest_rate) ** periods
        ) / ((1 + monthly_interest_rate) ** periods - 1)

        overpayment = annuity_payment * periods - principal
        print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
        print(f"Overpayment = {math.ceil(overpayment)}")

    @staticmethod
    def calculate_annuity_principal(periods: int, payment: float, interest: float) -> None:
        """Calculate the principal of a loan.

        Parameters:
        - periods: number of months during which the loan will be repaid
        - payment: annuity payment
        - interest: interest rate on a loan, expressed as a decimal fraction
        """

        monthly_interest_rate = interest / 12
        principal = payment / (
            (monthly_interest_rate * (1 + monthly_interest_rate) ** periods)
            / ((1 + monthly_interest_rate) ** periods - 1)
        )

        overpayment = payment * periods - principal
        print(f"Your loan principal = {math.floor(principal)}!")
        print(f"Overpayment = {math.ceil(overpayment)}")

    @staticmethod
    def calculate_annuity_periods(principal: float, payment: float, interest: float) -> None:
        """Calculate the number of months needed to repay a loan.

        Parameters:
        - principal: initial principal of the loan
        - payment: annuity payment
        - interest: interest rate on a loan, expressed as a decimal fraction
        """

        monthly_interest_rate = interest / 12
        periods = math.log(
            payment / (payment - monthly_interest_rate * principal),
            1 + monthly_interest_rate,
        )

        overpayment = payment * math.ceil(periods) - principal
        periods = math.ceil(periods)
        if periods < 12:
            print(f"It will take {periods} months to repay this loan!")
        else:
            months = periods % 12
            years = periods // 12
            if months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(
                    f"It will take {years} years and {months} months to repay this loan!")
        print(f"Overpayment = {math.ceil(overpayment)}")

    def diff_calc_load(self) -> None:
        """Calculate differentiated payments."""
        if self.payment:
            self.parser.error(
                "Incorrect parameters: --payment is not allowed with --type=diff")
        if not self.periods:
            self.parser.error(
                "Incorrect parameters: --periods is required with --type=diff")
        if not self.principal:
            self.parser.error(
                "Incorrect parameters: --principal is required with --type=diff")
        self.calculate_differentiated_payments(
            self.periods, self.principal, self.percent_interest)

    def annuity_calc_load(self) -> None:
        """Calculate annuity payments."""
        if self.payment and self.periods:
            self.calculate_annuity_principal(
                self.periods, self.payment, self.percent_interest)
        elif self.principal and self.periods:
            self.calculate_annuity_payment(
                self.periods, self.principal, self.percent_interest)
        elif self.principal and self.payment:
            self.calculate_annuity_periods(
                self.principal, self.payment, self.percent_interest)
        else:
            self.parser.error(
                "Incorrect parameters: --payment, --principal \
                and --periods are required with --type=annuity")

    def load(self) -> None:
        """Load credit calculator"""
        match self.type:
            case "diff":
                self.diff_calc_load()
            case "annuity":
                self.annuity_calc_load()
