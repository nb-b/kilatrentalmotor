file_path = "e:/JOBS/rentalmotorbanyuwangi/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = '''                                <span class="text-body text-text-body font-medium">/hari</span>
                            </div>
                        </div>
                        <button'''

replacement = '''                                <span class="text-body text-text-body font-medium">/hari</span>
                            </div>
                            </div>
                        </div>
                        <button'''

new_content = content.replace(target, replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Layout fixed!")
