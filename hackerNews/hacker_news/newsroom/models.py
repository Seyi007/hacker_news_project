from django.db import models
from django.urls import reverse

# Create your models here.
class Story(models.Model):
	"""Model representing the data fields to sync
	with the news fields from Hacker news"""
	story_id = models.IntegerField(blank=True, null=True)
	story_type = models.CharField(max_length=300, blank=True, null=True)
	by = models.CharField(max_length=300, blank=True, null=True)
	kids = models.IntegerField(null=True, blank=True)
	time = models.DateField(blank=True, null=True)
	url = models.CharField(max_length=300, blank=True, null=True)
	score = models.IntegerField(blank=True, null=True)
	title = models.CharField(max_length=300, blank=True, null=True)
	descendant = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.title

	@property
	def comment_count(self):
		return self._comment_set.count()

	def get_absolute_url(self):
		"""Returns the URL to access a particular instance of the model."""
		return reverse('story-detail', args=[str(self.id)])
	class Meta:
		ordering = ['-time']

class Comments(models.Model):
	"""Model that stores the comment from the story field"""
	story = models.ForeignKey('Story', on_delete=models.SET_NULL, null=True)
	by = models.CharField(max_length=500, blank=True, null=True)
	comment_id = models.IntegerField(blank=True, null=True)
	text = models.TextField(max_length=5000, blank=True, null=True)
	kids = models.IntegerField(null=True, blank=True)
	time = models.DateField(blank=True, null=True)
	comment_type = models.CharField(max_length=200, blank=True, null=True)
	parent = models.IntegerField(default=00, blank=True, null=True)

	def get_absolute_url(self):
		"""Returns the URL to access a particular instance of the model."""
		return reverse('comments-detail', args=[str(self.id)])

class Ask(models.Model):
	"""Model that represents the asks data"""
	by = models.CharField(max_length=500, blank=True, null=True)
	ask_id = models.IntegerField(blank=True, null=True)
	text = models.TextField(max_length=5000, blank=True, null=True)
	kids = models.IntegerField(null=True, blank=True)
	time = models.DateField()
	item_type = models.CharField(max_length=500, blank=True, null=True)
	score = models.IntegerField(blank=True, null=True)
	descendant = models.IntegerField(blank=True, null=True)
	title = models.CharField(max_length=500, blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		"""Returns the URL to access a particular instance of the model."""
		return reverse('ask-detail', args=[str(self.id)])

	class Meta:
		ordering = ['-time']


class askComments(models.Model):
	"""Model that store the comments on the ask item"""
	ask = models.ForeignKey('Ask', on_delete=models.SET_NULL, null=True)
	by = models.CharField(max_length=500, blank=True, null=True)
	comment_id = models.IntegerField(blank=True, null=True)
	kids = models.IntegerField(null=True, blank=True)
	parent = models.IntegerField(default=00, blank=True, null=True)
	text = models.TextField(max_length=5000, blank=True, null=True)
	time = models.DateField()
	kid_type = models.CharField(max_length=500, blank=True, null=True)

	def get_absolute_url(self):
		"""Returns the URL to access a particular instance of the model."""
		return reverse('askcomment-detail', args=[str(self.id)])

class Job(models.Model):
	"""Model that stores the jobs data"""
	by = models.CharField(max_length=500, blank=True, null=True)
	job_id = models.IntegerField(default=0, blank=True, null=True)
	text = models.TextField(max_length=5000, blank=True, null=True)
	time = models.DateField()
	item_type = models.CharField(max_length=500, blank=True, null=True)
	score = models.IntegerField(default=0, blank=True, null=True)
	title = models.CharField(max_length=500, blank=True, null=True)
	url = models.CharField(max_length=500, blank=True, null=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		"""Returns the URL to access a particular instance of the model."""
		return reverse('job-detail', args=[str(self.id)])

	class Meta:
		ordering = ['-time']