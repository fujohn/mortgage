def monthly_payment(principal, rate, term_months):
	"""
	Returns the monthly payment amount given the principal, monthly rate, and term.

	>>> monthly_payment(200000, 0.065 / 12, 360)
	1264.14

	"""
	monthly_rate = rate / 12
	if monthly_rate != 0:
		monthly_cost = (monthly_rate * principal * ((1 + monthly_rate)**term_months)) / (((1 + monthly_rate)**term_months) - 1)
		return round(monthly_cost, 2)
	else:
		monthly_cost = principal / term_months
		return round(monthly_cost, 2)


def amortization_schedule(principal, monthly_payment, rate):
	"""
	Returns a dictionary where the key represents the month into the term (N) and the value is a list [Interest, principal paid, remaining principal]
	"""
	amortization = {}
	monthly_rate = rate / 12
	month_into_term = 0
	while principal > 0:
		month_into_term += 1
		interest = principal * monthly_rate
		principal_paying = min(monthly_payment - interest, principal)
		principal -= principal_paying
		amortization[month_into_term] = [round(interest, 2), round(principal_paying, 2), round(principal, 2)]
	return amortization
		
