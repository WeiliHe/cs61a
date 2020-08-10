; Q4
(define (rle s)
  (define helper (prev counts right)
    (if (null? right)
      (cons-stream (list prev counts) nil)
      (if (= prev (car right))
        (helper prev (+ counts 1) (cdr-stream right))
        (cons-stream (list prev counts) (helper (car right ) 1 (cdr-stream right)))
    )))
  (if (null? s)
    (nil)
    (helper ((car s) 1 (cdr-stream right))))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
; (define (insert n s)
;   (cond ((= n (car s)) s)
;       ((null? s) (cons n nil))
;       ((< n (car s)) (append `(,n) s))
;       (else (cons (car s) (insert n (cdr s))))
;     )
; )

; Q5 tail call
(define (insert n s)
  (define (helper left n right)
    (if (null? right)
      (append left (list n))
      (if (< n (car right))
        (append left (list n) right)
        (helper (append left (list (car right))) n (cdr right)))
      )
    )
  (helper nil n s)
)


; Q6
(define (deep-map fn s)
  (if (null? s)
    nil
    (if (list? (car s))
      (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
      (cons (fn (car s)) (deep-map fn (cdr s))))
    )
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  (if (null? s)
    nil
    (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s))) )
    )
)

(define (count name s)
  (define (helper num name s)
    (if (null? s)
      0
      (if (not (eq? name (car s)))
        (helper num name (cdr s))
        (+ 1 (helper num name (cdr s)))
        )
      )
    )
  (helper 0 name s)
)

(define (tally names)
  (define (helper unique_s s)
    (if (null? unique_s)
      nil
      (cons (cons (car unique_s) (count (car unique_s) s)) (helper (cdr unique_s) s)))
    )
  (if (null? names)
    nil
    (helper (unique names) names))
)