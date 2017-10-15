Repository related to https://github.com/szabgab/modiin-co-learning/

## Task

* Fork and clone this repository
* Run the tests on your own computer

```
$ python -m unittest discover
```

You should see an error like this:

```
.F
======================================================================
FAIL: test_sum (my.test_math.TestMy)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../python-with-test/my/test_math.py", line 9, in test_sum
    self.assertEqual(my.math.sum(2, 3, 4), 6)
AssertionError: 9 != 6

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

Find the incorrect test function, comment it out (by adding a `#` in front of the problematic lines
and run the tests again. This time you should see something like this:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

* Then set up Travis-CI for this project. Create the `.travis.yml` file, configure the Travis-CI service.
* Once Travis works in your own GitHub/Travis-CI accounts, send a pull-request.
* We will comment on the PR, but won't merge it.
* The `script` part must be the command we use to run the tests. In our case this is `python -m unittest discover`.
