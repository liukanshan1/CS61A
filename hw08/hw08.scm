(define (my-filter func lst)
    (if (null? lst)
        nil
        (if (func (car lst))
            (cons (car lst) (my-filter func (cdr lst)))
            (my-filter func (cdr lst))
        )
    )
)

(define (my-filter2 func lst)
    (if (null? lst)
        nil
        (if (func (car lst) lst)
            (cons (car lst) (my-filter2 func (cdr lst)))
            (my-filter2 func (cdr lst))
        )
    )
)

(define (interleave s1 s2) 
    (if (and (not (null? s1)) (not (null? s2)))
        (append (list (car s1) (car s2)) (interleave (cdr s1) (cdr s2))) 
        (if (null? s1) s2 s1)
    )
)

(define (accumulate merger start n term)
  (if (> n 0)
    (accumulate merger (merger start (term n)) (- n 1) term)
    start
  )
)

(define (no-repeats lst) 
  (my-filter2 no-repeats-filter lst)
)

(define (no-repeats-filter item lst)
  (if (null? (cdr lst))
    #t
    (if (= item (car (cdr lst)))
      #f
      (no-repeats-filter item (cdr lst))
    )
  )
)
