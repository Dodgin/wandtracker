import cv2
import numpy as np
from pprint import pprint
import os

# Provides wand gesture processing capabilities
class Gesture:

    # Constructor
    def __init__(self):
        self.spell_dir = os.path.join(os.path.dirname(__file__),'..',
            'source_material','spells')
        self.MIN_MATCH_COUNT = 5
        self.sift = cv2.xfeatures2d.SIFT_create()
        self.spell_dict = {}    # lookup table for spells ID => (cv2.img)
        self.loadSpellDictionary()

    # returns this gesture's context if any
    def getContext(self):
        return 0

    # loads the spell dictionary from ../source_material/spells
    def loadSpellDictionary(self):
        print("\nLoading spell dictionary...")
        for filename in os.listdir(self.spell_dir):
            if filename.endswith(".png"):
                spellkey = os.path.splitext(filename)[0]
                print('Importing spell ' + spellkey + '... ', end="", flush=True)
                spell_fp = os.path.join(self.spell_dir, filename)
                self.spell_dict[spellkey] = cv2.imread(spell_fp,0)
                if(self.spell_dict[spellkey] is not None):
                    print('imported!')


    # returns the result of self.raw_wand_data against the spell database
    def toSpell(self, gesture_cv_img):

        print("\nConverting gesture to spell...")

        # Highest spell likelihood
        most_likely_spell = None
        most_likely_featurematches = 0

        # Iterate through the spells and run FLANN
        for spell_key, spell in spell_dict.items():
            featurematches = self.siftFlann(gesture_cv_img, spell)
            if(most_likely_featurematches < featurematches):
                most_likely_spell = spell_key
                most_likely_featurematches = featurematches

        # Return logic
        if(most_likely_spell = None):
            return False
        else return most_likely_spell


    # SIFT FLANN function to return a metric of likeness
    def siftFlann(img_user, img_dict):

        # find the keypoints and descriptors with SIFT
        kp1, des1 = self.sift.detectAndCompute(img_dict,None)
        kp2, des2 = self.sift.detectAndCompute(img_user,None)

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 200)

        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(des1,des2,k=2)

        # store all the good matches as per Lowe's ratio test.
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)

        featurematches = len(good)
        print("Feature matches found: " + str(featurematches))

        return featurematches
