from silence.decorators import endpoint

@endpoint(
    route="/subjects",
    method="GET",
    sql="SELECT * FROM subjects",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/subjects/$departmentId",
    method="GET",
    sql="SELECT * FROM subjects WHERE departmentId = $departmentId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/subjects",
    method="POST",
    sql="INSERT INTO subjects (name, city) VALUES ($name, $city)",
    auth_required=True,
)
def add(name, city):
    pass

###############################################################################

@endpoint(
    route="/subjects/$departmentId",
    method="PUT",
    sql="UPDATE subjects SET name = $name, city = $city WHERE departmentId = $departmentId",
    auth_required=True,
)
def update(name, city):
    pass

###############################################################################

@endpoint(
    route="/subjects/$departmentId",
    method="DELETE",
    sql="DELETE FROM subjects WHERE departmentId = $departmentId",
    auth_required=True,
)
def delete():
    pass