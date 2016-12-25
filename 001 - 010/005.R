lcm <- function(a, b) {
  # calculate gcd
  for (i in seq(b, 1, by = -1)) {
    if (b %% i == 0 && a %% i == 0) {
      return(a*b/i)
    }
  }
  return(a*b)
}

result <- 2520 # lcm of 1 through 10

for (i in seq(11, 20)) {
  if (result %% i != 0) {
    result <- lcm(i, result)
  }
}

print(result)
