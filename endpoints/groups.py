from silence.decorators import endpoint

@endpoint(
    route="/groups",
    method="GET",
    sql="SELECT * FROM groups",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/groups/$groupsId",
    method="GET",
    sql="SELECT * FROM groups WHERE groupsId = $groupsId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/groups",
    method="POST",
    sql="INSERT INTO groups (name, city) VALUES ($name, $city)",
    auth_required=True,
)
def add(name, city):
    pass

###############################################################################

@endpoint(
    route="/groups/$groupsId",
    method="PUT",
    sql="UPDATE groups SET name = $name, city = $city WHERE groupsId = $groupsId",
    auth_required=True,
)
def update(name, city):
    pass

###############################################################################

@endpoint(
    route="/groups/$groupsId",
    method="DELETE",
    sql="DELETE FROM groups WHERE groupsId = $groupsId",
    auth_required=True,
)
def delete():
    pass