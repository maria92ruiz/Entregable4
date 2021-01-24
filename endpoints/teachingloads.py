from silence.decorators import endpoint

@endpoint(
    route="/teachingloads",
    method="GET",
    sql="SELECT * FROM teachingloads",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/teachingloads/$departmentId",
    method="GET",
    sql="SELECT * FROM teachingloads WHERE departmentId = $departmentId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/teachingloads",
    method="POST",
    sql="INSERT INTO teachingloads (name, city) VALUES ($name, $city)",
    auth_required=True,
)
def add(name, city):
    pass

###############################################################################

@endpoint(
    route="/teachingloads/$departmentId",
    method="PUT",
    sql="UPDATE teachingloads SET name = $name, city = $city WHERE departmentId = $departmentId",
    auth_required=True,
)
def update(name, city):
    pass

###############################################################################

@endpoint(
    route="/teachingloads/$departmentId",
    method="DELETE",
    sql="DELETE FROM teachingloads WHERE departmentId = $departmentId",
    auth_required=True,
)
def delete():
    pass