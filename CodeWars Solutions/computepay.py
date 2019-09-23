def computepay(h,r):
	if h > 40:
		overtime = h % 40
		hours = h-overtime
		return((hours * r) + (overtime * r)*1.5)
	return "Payout: ", float(h) * float(r)

print(computepay(float(raw_input("hour: ")), float(raw_input("payrate: "))))

# 5 * 10.5 *1.5
# 78.75
# 420
# -----------
# 498.75



