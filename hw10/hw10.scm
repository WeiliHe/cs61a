(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

; dont quite understand, what if the combiner is + and the term  is square, start is 1
; does it mean 1 + 1^2, + （1 + 2^2）?
(define (accumulate-tail combiner start n term)
  (if (= n 0))
  	start
  	(accumulate-tail combiner (combiner start term(n)) (- n 1) term)
)

(define-macro (list-of expr for var in seq if filter-fn)
  ; 'YOUR-CODE-HERE
  (list 'map (list 'lambda (list var) expr) (list 'filter (list 'lambda list(var) filter-fn) seq))
)