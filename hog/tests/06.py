test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': '5e0e1a4c94a7429afae6399105d34f05',
          'choices': [
            'Another commentary function.',
            'An integer representing the score.',
            'None.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does a commentary function return?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)
          d7882c94106188a2f424c5383b507923
          072ed6d8c8b94db1f2452887d165717d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def count(n):
          ...     def say(s0, s1):
          ...         print(n, s0)
          ...         return count(n + 1)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=15, say=count(1))
          61f188e55077f84722da3594df10f844
          072a7e5a36da4da6069d77fa89868297
          f94e83d9efe9e8103c61bab16ee53943
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          f4d41f4e29a08f003e0a9a5473c61d5e
          461ff541bd06a2e3310447d10cc6615b
          f60c6fb3960edbba415a62b9e4340f1c
          b4a0c241b24ecd8a462abb008ea839af
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
          accd0f5c57e0f3fad13791aaecafc38b
          c42887e7b9ffe8fc26bb57b61329f916
          cbe9649db9e3fa2aa95c8f2df21707e5
          26dad951f8e75106f151e4085e117edd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))
          3f321d5ce997d2f3989685f56de8bdce
          4a64fe964dc771a219ed773c3a146c75
          3f321d5ce997d2f3989685f56de8bdce
          cad0f4cdee6d8af26abb184d977c50fd
          493e127f779e284556086802640185a8
          cad0f4cdee6d8af26abb184d977c50fd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes()))
          Player 0 now has 1 and Player 1 now has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and Player 1 now has 2
          Player 1 takes the lead by 1
          Player 0 now has 4 and Player 1 now has 2
          Player 0 takes the lead by 2
          Player 0 now has 4 and Player 1 now has 10
          Player 1 takes the lead by 6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
