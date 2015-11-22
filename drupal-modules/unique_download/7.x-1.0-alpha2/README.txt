UNIQUE DOWNLOAD
---------------------------

Install
-------
Steps :
1. Download and extract the module into sites/all/modules directory.
2. Enable the module from admin/build/modules using admin login.
3. You are ready to use the unique download module.
4. There will be menu item available in drupal navigation "Unique URL settings".



Description
-----------

This module is used to generate the unique / one time links to download for specific file.
For now there is very basic hashing algorithm used in this module to generate the hashkey.



Settings
-------- 

Basic settings for modules are located under :
http://<yoursite>/admin/config/system/unique

There is option for Multiple download : If you want users can download this file multiple times you can check this option and users will be able to download it multiple times. This feature is limited currently.

It allows you to select the content type to which the file is bound. you can select one or more content types from the existing content types of your site.

Path : This is where you are storing the files under public:// folder or any stream oriented folders which you have under public://
For instance : public://fields/uniquefiles

To generate the Unique URL:
click on the Generate unique URL tab present under settings it will take you to 
http://<yoursite>/admin/config/system/unique/generate

Here you need to specify following things to generate unique URL:
1. node id of a node to which file is associated.
2. Email address to whom you need to send an email after generating the URL (currently in dev).
3. Expiry of the generated URL.

To see all the generated unique URLs and their status:
http://<yoursite>/admin/config/system/unique/download

It will show all the data related to the URL including email, expiry, generated uniqueURL, no. of downloads done etc in the tabular format.

