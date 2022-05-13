test = {
  'name': 'Self-Reference',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def crust():
          ...   print("70km")
          ...   def mantle():
          ...       print("2900km")
          ...       def core():
          ...           print("5300km")
          ...           return mantle()
          ...       return core
          ...   return mantle
          >>> drill = crust
          >>> drill = drill()
          cb9c2df3a4cb7a5551c73372025903f1
          # locked
          >>> drill = drill()
          fec7434f7090fafe15bc6dec9bf46bf1
          # locked
          >>> drill = drill()
          fcce62b963fdb83e20f9b0a5de62abdc
          fec7434f7090fafe15bc6dec9bf46bf1
          # locked
          >>> drill()
          fcce62b963fdb83e20f9b0a5de62abdc
          fec7434f7090fafe15bc6dec9bf46bf1
          659ff188e141211878c9838e1df2c80e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
