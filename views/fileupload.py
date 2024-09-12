from flask import Flask, render_template, request

def view_fileupload(app):
    @app.route('/fileuplod', methods=['GET', 'POST'])
    def fileuplod():
        return render_template('upload/fileuplod.html')