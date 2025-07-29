import sys
import warnings

from datetime import datetime

from crew import AiNewsScraper

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'last 24 hours news',
        'current_year': str(datetime.now().year),
        'date': datetime.now().strftime('%Y-%m-%d'),
    
    }
    
    try:
        AiNewsScraper().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()