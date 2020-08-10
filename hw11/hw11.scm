(define (find s predicate)
	(if (null? s)
	    #f
  		(if (predicate (car s))
  			(car s)
  			(find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (if (null? s)
  	nil
  	(cons-stream (* (car s)  k) (scale-stream (cdr-stream s) k)))
)

(define (has-cycle s)
	(define (helper fast slow)
		(cond ((or (null? fast) (null? (cdr-stream fast))) #f)
			((eq? fast slow) #t)
			(else (helper (cdr-stream (cdr-stream fast)) (cdr-stream slow)))))
	(helper (cdr-stream s) s)
)
(define (has-cycle-constant s)
	(define (helper fast slow)
		(cond ((or (null? fast) (null? (cdr-stream fast))) #f)
			((eq? fast slow) #t)
			(else (helper (cdr-stream (cdr-stream fast)) (cdr-stream slow)))))
	(helper (cdr-stream s) s)
)
