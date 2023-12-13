#!/usr/bin/python3
""" objects that handle all default RestFul API actions"""
from models.favorite import Favorites
from models.recipe import Recipe
from models.category import Category
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/recipes', methods=['GET'], strict_slashes=False)
def get_recipes():

    all_recipes = storage.all(Recipe).values()
    list_r = []
    for recipe in all_recipes:
        list_r.append(recipe.to_dict())
    return jsonify(list_r)

@app_views.route('/recipes/<type_id>', methods=['GET'], strict_slashes=False)
def get_recipesbytype(type_id):

    all_recipes = storage.getrecipesbytype(type_id).values()
    list_r = []
    for recipe in all_recipes:
        list_r.append(recipe.to_dict())
    return jsonify(list_r)

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():

    all_categories = storage.all(Category).values()
    list_r = []
    for category in all_categories:
        list_r.append(category.to_dict())
    return jsonify(list_r)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'device_id' not in request.get_json():
        abort(400, description="Missing device id")
   
    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/add.favorite', methods=['POST'], strict_slashes=False)
def post_favorite():
    """
    Creates a favorite
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user id")
    if 'recipe_id' not in request.get_json():
        abort(400, description="Missing recipe id")
   
    data = request.get_json()
    instance = Favorites(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/favorites/<id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_favorite(id):
    """
    Deletes an Object
    """

    favorite = storage.get(Favorites, id)

    if not favorite:
        abort(404)

    storage.delete(favorite)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/favorites/<user_id>', methods=['GET'], strict_slashes=False)
def get_userfavorites(user_id):

    all_recipes = storage.getuserfavorites(user_id).values()
    list_r = []
    for recipe in all_recipes:
        list_r.append(recipe.to_dict())
    return jsonify(list_r)
