(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s))
)

(define (caddr s) 
    (car (cdr (cdr s)))
)

(define (ordered? s) 
    (if (null? s) 
        #t
        (if (null? (cdr s))
            #t
            (if (not (> (car s) (cadr s)))
                (ordered? (cdr s))
                #f
            )
        )

    )
)

(define (square x) (* x x))

(define (pow base exp) 
    (if (= exp 1)
        base
        (if (even? exp)
            (pow (square base) (/ exp 2))
            (* base (pow (square base) (/ (- exp 1) 2)))
        )
    )
)
