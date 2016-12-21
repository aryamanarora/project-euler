# 15.886 seconds, want to reduce this...
# even slower than Python!
is.palindromic <- function(x) {
  return(grepl('^([0-9])([0-9])([0-9])\\3\\2\\1$', x))
}

answer <- 0
for (i in 100:999) {
  for (j in 100:999) {
    if (is.palindromic(i*j) & i*j > answer) {
      answer <- i*j
    }
  }
}
print(answer)
