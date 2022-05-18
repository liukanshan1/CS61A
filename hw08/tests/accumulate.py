test = {
  'name': 'accumulate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (accumulate * 1 5 identity)
          b68dcf8d10adeb9d824d591b9fa02a67
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define (identity x) x)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define (square x) (* x x))
          8a2a6f52fb7521b1c0b25994a9773f92
          # locked
          scm> (accumulate + 0 5 square)
          c463ce57625b4ac368d810a444968ed2
          # locked
          scm> (accumulate + 5 5 square)
          da469c509712bc943dfbbdeb2ddf6883
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
