# Pollango Django App

<em>See Documentation and tutorial references at:</em> https://docs.djangoproject.com/en/5.1/intro/tutorial02/

<h4>This is a simple Django polling app that demonstrates how to create and interact with `Question` and `Choice` models using Django's ORM. Below is an overview of some common actions you can perform.
</h4>
## Setting Up

### 1. Create a Question
You can create a new `Question` object by specifying the question text and the publication date.

```python
from django.utils import timezone
from polls.models import Question

# Create a new Question object.
q = Question(question_text="What's up?", pub_date=timezone.now())
q.save()
2. Querying the Question Model
Get all questions:

python
Copy
Question.objects.all()
Output:
<QuerySet [<Question: What's up?>]>

Get the first question:

python
Copy
Question.objects.first()
Get the last question:

python
Copy
Question.objects.last()
Get a specific question by ID:

python
Copy
Question.objects.get(id=1)
3. Filtering Questions
Django provides a rich database lookup API that is driven by keyword arguments.

Get questions by specific criteria:

python
Copy
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith="What")
Get questions published in the current year:

python
Copy
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
Error handling when a question ID doesn’t exist:

python
Copy
Question.objects.get(id=2)  # Raises DoesNotExist exception
Using primary key (pk) shortcut for lookups:

python
Copy
Question.objects.get(pk=1)
4. Custom Methods
Django allows you to define custom methods on models. For instance, we define was_published_recently as a custom method for the Question model.

python
Copy
q = Question.objects.get(pk=1)
q.was_published_recently()
Creating Choices for a Question
1. Adding Choices to a Question
You can associate Choice objects with a Question. Django provides a related object set (choice_set) to access the choices for a given question.

Creating choices:

python
Copy
q = Question.objects.get(pk=1)

# Create three choices.
q.choice_set.create(choice_text="Not much", votes=0)
q.choice_set.create(choice_text="The sky", votes=0)
c = q.choice_set.create(choice_text="Just hacking again", votes=0)
2. Accessing Related Choices
Once the choices are created, you can access them through the related object set.

python
Copy
# Display choices for the question.
q.choice_set.all()

# Count the number of choices for the question.
q.choice_set.count()
3. Accessing the Related Question from a Choice
Choices are related to a specific question, and you can access the related question like this:

python
Copy
# Access the related question from a choice object.
c.question
4. Querying Choices Based on Relationships
You can query Choice objects based on the properties of the related Question object.

python
Copy
Choice.objects.filter(question__pub_date__year=current_year)
5. Deleting Choices
To delete a choice, you can use the delete() method on a filtered queryset.

python
Copy
# Delete a choice.
c = q.choice_set.filter(choice_text__startswith="Just hacking")
c.delete()
Conclusion
This Django app demonstrates basic functionality for creating and interacting with questions and choices in a polling application. You can use the provided methods to filter, query, and manipulate the data stored in the database.

Additional Resources
For more information on Django models and querying the database, visit the official Django documentation.

vbnet
Copy

This `README.md` gives a detailed overview of how to use the `Question` and `Choice` models, covering all the example operations you mentioned. Let me know if you'd like to add or change anything!