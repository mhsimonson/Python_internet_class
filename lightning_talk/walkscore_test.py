import math
import copy
from walkscore.scoring.profile import Profile
import walkscore.scoring.scale
amenities_by_locale = {}
amenities_by_locale[None] = {
"grocery": {"api": "google", "search": ["grocery store"]},
"restaurants": {"api": "google", "search": ["restaurant"]},
"coffee": {"api": "google", "search": ["cafe"]},
"bars": {"api": "google", "search": ["pub"]},
"movies": {"api": "google", "search": ["cinema"]},
"schools": {"api": "google", "search": ["school"]},
"parks": {"api": "google", "search": ["parks"]},
"libraries": {"api": "google", "search": ["library"]},
"books": {"api": "google", "search": ["bookstore"]},
"fitness": {"api": "google", "search": ["fitness"]},
"pharmacies": {"api": "google", "search": ["pharmacy"]},
"retail": {"api": "google", "search": ["retail"]},
{amenities_by_locale['us'] (amenities_by_locale[None],
coffee={"api": "google", "search": ["coffee shop"]},
bars={"api": "google", "search": ["bar"]},
movies={"api": "google", "search": ["movie theater"]},
schools={"api": "education"},
parks={"api": "parks"},
pharmacies={"api": "google", "search": ["drug store"]},
hardware={"api": "google", "search": ["hardware store"]},
(
amenities_by_locale['ca'] (amenities_by_locale[None],
parks={"api": "parks"},
(
amenities_by_locale['gb'] = amenities_by_locale['ca']
amenities_by_locale['ie'] = amenities_by_locale['ca']
amenities_by_locale['au'] = amenities_by_locale['ca']
amenities_by_locale['nz'] = amenities_by_locale['ca']
class WalkscoreV1(Profile):
identifier = "walkscore"
version = 1
locale = None
name = "Walk Score"
brief = "Walk Score v1"
metrics = {
"amenities": {
"type": "amenities",
"amenities": amenities_by_locale[None],
"measurer": {
"name": "great_circle",
,{
"scale": {
"type": "step",
"steps": [0.25, 0.5, 0.75, 1.0],
"values": [100.0, 80.0, 40.0, 20.0, 0.0]
,{
,{
{
model = [
}
"metric": "amenities",
"scale": None
{
[
def __init__(self, locale=None):
"""
This profile is localizable. Initialize with a supported locale to
customize the amenity queries.
"""
super(WalkscoreV1, self).__init__()
