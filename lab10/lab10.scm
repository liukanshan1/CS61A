(define (over-or-under num1 num2) 
     (cond ((< num1 num2) (- 1))
        ((= num1 num2) 0)
        (else 1)
     )
)

(define (make-adder num) 
    (lambda (x) (+ x num))
)

(define (composed f g) 
    (lambda (x) (f (g x)))
)

(define lst 
    (list (list 1) 2 (list 3 4) 5)
)

(define (remove item lst) 
    (if (null? lst) 
        ()
        (car (list (filter (lambda (x) (not (= x item))) lst)))
    )
)
