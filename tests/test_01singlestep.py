import unittest, json
from stairstep import StairStep, State

class TestStepFunctionWithSingleStep(unittest.TestCase):
    def test_single_state(self):
        self.maxDiff = None
        output = '''
            {
                "Comment": "A simple minimal example of the States language",
                "StartAt": "Hello World",
                "States": {
                    "Hello World": { 
                        "Type": "Task",
                        "Resource": "arn:aws:lambda:us-east-1:123456789012:function:HelloWorld",
                        "Next": "nextResource"
                    }
                }
            }
        '''
        #compress and remove whitespace
        output = json.dumps( json.loads(output) )
        ss = StairStep(
            comment = "A simple minimal example of the States language",
            startAt = "Hello World",
        )
        hello_step = State(
            name = "Hello World",
            stype = "Task",
            resource = "arn:aws:lambda:us-east-1:123456789012:function:HelloWorld",
            snext = "nextResource"
        )

        ss.addState(hello_step)
        self.assertEqual(output, ss.json())

    def test_single_state_comment_optional(self):
        output = '''{
                        "StartAt": "Hello World",
                        "States": {
                            "Hello World": { 
                                "Type": "Succeed",
                                "Resource": "arn:aws:lambda:us-east-1:123456789012:function:HelloWorld"
                            }
                        }
                    }'''
        #compress and remove whitespace
        output = json.dumps( json.loads(output) )
        ss = StairStep(
            startAt = "Hello World",
        )
        hello_step = State(
            name = "Hello World",
            stype = "Succeed",
            resource = "arn:aws:lambda:us-east-1:123456789012:function:HelloWorld",
        )

        ss.addState(hello_step)
        self.assertEqual(output, ss.json())

class TestStepFunctionWithoutSteps(unittest.TestCase):
    def setUp(self):
        self.output = {
                "Type": "Succeed",
                "Resource": "arn:aws:lambda:us-east-1:123456789012:function:HelloWorld",
            }

    def test_no_states(self):
        hello_step = State(
            name = "Hello World",
            stype = "Succeed",
            resource = "arn:aws:lambda:us-east-1:123456789012:function:HelloWorld",
        )
        self.assertEqual( hello_step.export(), self.output )
