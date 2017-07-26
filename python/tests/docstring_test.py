import nose.tools as nt

import pandas as pd
import docstring

def test_docstring():
  data = "Myeong"
  output = docstring.test(False, False, data)

  nt.assert_equal(output, "Myeong")