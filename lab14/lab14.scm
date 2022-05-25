(define (split-at lst n)
  (define (split lst n)
    (if (> n 0)
      (split (cons (append (car lst) (list (car (cdr lst)))) (cdr (cdr lst))) (- n 1))
      (list (car lst) (cdr lst))
    )
  )
  (split (append (list (list )) lst) n)
)

(define (compose-all funcs)
  (define (compose x)
    (if (null? funcs)
      x
      ((compose-all (cdr funcs)) ((car funcs) x))
    )
  )
  compose
)
