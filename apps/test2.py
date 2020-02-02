# ourList = []
# firstDic = {'img':'sflkj'}
# twoDic = {2:'sdlfkjkls'}

# ourList.append(firstDic.copy())
# print(ourList)
# ourList.append(twoDic.copy())
# print(ourList)

hemispheres = [{'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg', 'title': 'Cerberus Hemisphere Enhanced'}, {'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg', 'title': 'Schiaparelli Hemisphere Enhanced'}, {'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg', 'title': 'Syrtis Major Hemisphere Enhanced'}, {'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg', 'title': 'Valles Marineris Hemisphere Enhanced'}]

print(hemispheres[0].get('title'))
print(hemispheres[0].get('img_url'))