func fib(n int) int {
	var mod int = 1e9 + 7
	if n < 2 {
		return n
	}
	p, q, sum := 0, 0, 1
	for i := 2; i <= n; i++ {
		p = q
		q = sum
		sum = (p + q) % mod
	}
	return sum
}