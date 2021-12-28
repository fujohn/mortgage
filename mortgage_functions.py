def monthly_payment(principal, monthly_rate, term_months):
	if monthly_rate != 0:
		return (monthly_rate * principal * ((1 + monthly_rate)**term_months)) / (((1 + monthly_rate)**term_months) - 1)
	else:
		return principal / term_months

