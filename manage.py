from app import create_app
from flask_script import manager, server
  
app = create_app('developement')

manager = manager(app)
manager.add_command('server',server)
@manager.command
def test():
  """Run the unit tests."""
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

  if __name__== '__main__':
    app.run   