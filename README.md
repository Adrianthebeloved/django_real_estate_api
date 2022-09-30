# Django Capstone Project

This repository is the final code for a basic Real estate website.

---

### Install Dependencies

1. **Python 3.8.10** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **Requirements** - All dependencies can be installed from the requirements.txt file.

## Running the Project

1. Create a virtual environment with `virtualenv venv`
2. Activate the environment with `source env/Scripts/activate`
3. Clone the project
4. Install dependencies with `pip install requirements.txt`
5. Provision a database on your Local machine
6. Make migtrations and migrate
6. Run the server with `python manage.py runserver`

## Listing Model

```
class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title
```

### CRUD Operations

## Listings List View
```
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)
```
- This function takes in a GET request and returns all the Objects of the Listing model and renders these objects on the corresponding HTML page.

## Listing View
```
def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)
```
- This function take in a GET request and the id of a particular listing and returns the listing with said id, and renders it on the corresponding HTML page

## Listing Create View
```
csrf_exempt
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)
```
- This function represents the view for creating a Listing object of the Listing model. 
Here we make use of Django's ModelForms to retrieve input from the User.
The function also has a csrf_exempt decorator to exempt it from csrf authentication, making it accessible to un-authenticated users

## Listing Update View
```
@csrf_exempt
def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)
```
- This function represents the view for updating a Listing. It takes a POST request and primary key parameters and returns the object at that particular ID for editing.

## Listing Delete
```
@csrf_exempt
def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")
```
- This function deletes a particular listing from the database.