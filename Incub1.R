runs <- 100000
one.trial <- function(){
  seq <- sample(1:4, 4)
  temp <- seq[1]
  count = 1
  for (i in 2:length(seq)) {
    if (is.element(seq[i] - 1, temp) | is.element(seq[i] + 1, temp)) {
      count = count + 1
    c(temp,seq[i])
    }
  }
}
one.trial()

