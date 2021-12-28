def monthly_payment(principal, monthly_rate, term_months):
	"""
	Returns the monthly payment amount given the principal, monthly rate, and term.

	>>> monthly_payment(200000, 0.065 / 12, 360)
	1264.14

	"""
	if monthly_rate != 0:
		monthly_cost = (monthly_rate * principal * ((1 + monthly_rate)**term_months)) / (((1 + monthly_rate)**term_months) - 1)
		return round(monthly_cost, 2)
	else:
		monthly_cost = principal / term_months
		return round(monthly_cost, 2)

