; Q1
(define (compose-all funcs)
  (if (null? funcs)
  	(lambda (x) x)
  	(lambda (x) (compose-all (cdr funcs)) ((car funcs) x))）
)

; Q2
(define (tail-replicate x n)
  (if (= n 0)
  	nil
  	(cons x (tail-replicate x n -1)))
)