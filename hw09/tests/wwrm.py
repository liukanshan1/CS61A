test = {
  'name': 'wwrm',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'd074f67b3b777b03ecc810123a1fbae1',
          'choices': [
            'Any 6-digit hexadecimal color code, like #fdb515',
            'A hexadecimal color code that starts with letters and ends with numbers, like #gg1234',
            'Any hexadecimal color code with 0-6 digits',
            'A hexadecimal color code with 3 letters and 3 numbers'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '#[a-f0-9]{6}'
        },
        {
          'answer': '4ed2cbe877f71b60b3007b745a7641b6',
          'choices': [
            'Only fizzbuzz',
            'Only fizz',
            'Only fizzbuzz, fizz, and buzz',
            'Only fizzbuzzbuzz',
            'Only fizzbuzz or buzz'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '(fizz(buzz|)|buzz)'
        },
        {
          'answer': '459cd95194a7e36b8f3d9bbd1b11e44f',
          'choices': [
            'Signed or unsigned numbers like +1000, -1.5, .051',
            'Only unsigned numbers like 0.051',
            'Only signed numbers like +1000, -1.5',
            'Only signed or unsigned integers like +1000, -33'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '`[-+]?\\d*\\.?\\d+`'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
