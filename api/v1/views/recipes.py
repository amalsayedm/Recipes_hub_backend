#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.recipe import Recipe
from models.category import Category
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
