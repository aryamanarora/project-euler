fibonacci <- numeric()
fibonacci[1] <- 1
fibonacci[2] <- 2
i <- 3

repeat {
  fibonacci[i] <- fibonacci[i-2] + fibonacci[i-1]
  if (fibonacci[i] > 4e6) break
  i <- i + 1
}

sum <- 0
for (num in 1:length(fibonacci)) {
  if (fibonacci[num] %% 2 == 0) {
    sum <- sum + fibonacci[num]
  }
}

print(sum)
