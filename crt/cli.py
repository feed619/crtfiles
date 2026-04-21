import click
from crt.option import crt_files
from crt.templates import create_template, delete_template, get_all_template_names, get_template, make_template, rename_template
from crt.tools import expand_user_path


@click.command()
@click.option("-t", "--temp", required=False, type=str, help="Template name to use")
@click.option("-v", "--view", is_flag=True, help="View all templates")
@click.option("-a", "--append", is_flag=True, help="Create new template with current directory content")
@click.option("-rm", "--remove", is_flag=True, help="Remove existing template")
@click.option("-rn", "--rename", type=str, help="Rename template name")
@click.option("-p", "--path", type=str, default=".", help="Target directory (default: current directory)")
@click.option("-f", "--fill", is_flag=True, help="Fill generated files with template content")
@click.argument(
    "oth",
    required=False,
)
@click.argument(
    "ext",
    required=False,
)
def main(temp, view, append, remove, rename, path, fill, oth, ext):

    full_path = expand_user_path(path)
    if not full_path.exists():
        full_path.mkdir(parents=True, exist_ok=True)

    # print(f"Options: temp={temp}, view={view}, append={append}, remove={remove},rename={rename}, path={path}, fill={fill}, oth={oth}, ext={ext}")
    if view:
        template_names = get_all_template_names()
        print("Available templates:")
        default_names = template_names.get("default_names", [])

        if default_names:
            print(" Default:")
            for name, count_files in default_names.items():
                if name == "gitignore":
                    template = get_template("gitignore")
                    ext_names = [ext_name for ext_name in template["ext"]]
                    print(f"  • {name} ({', '.join(ext_names)})")
                else:
                    print(f"  • {name} ({count_files} files)")

        custom_names = template_names.get("custom_names", [])
        if custom_names:
            print(" Custom:")
            for name, count_files in custom_names.items():
                print(f"  • {name} ({count_files} files)")

    elif temp:
        template = get_template(temp)
        if rename:
            if not template:
                print(f"Template '{temp}' not found")
                return

            if get_template(rename):
                print(f"Template '{rename}' already exist")
                return

            if rename_template(template_name=temp, new_name=rename):
                print(f"Template renamed: '{temp}' → '{rename}'")
            else:
                print(f"You can't rename default template '{temp}'")

        # Append mode - create new template from current directory
        elif append:
            if template:
                print(f"Template '{temp}' already exists!")
                return
            if create_template(temp_name=temp, path=full_path):
                print(f"Template '{temp}' created successfully from: {full_path}")
                return
            else:
                print(f"Failed to create template '{temp}'")
                return

        # Remove mode - delete existing template
        elif remove:
            if not template:
                print(f"Template '{temp}' not found!")
                return
            if delete_template(template_name=temp):
                print(f"Template '{temp}' removed successfully!")
                return
            else:
                print(f"You can't remove default template '{temp}'")
                return

        # Default mode - use existing template
        else:
            if not template:
                print(f"Template '{temp}' not found!")
                print(f"Use --append flag to create this template")
                return
            else:
                if temp == "gitignore":
                    if not oth:
                        print("Error: Please provide an extension for the gitignore template")
                    else:
                        if oth not in template.get("ext", {}):
                            print(f"Error: Gitignore template '{oth}' not found")
                        else:
                            template["files"][".gitignore"] = template["ext"].get(oth)
                            if make_template(base_dir=full_path, template=template, fill=True):
                                print(f"{oth} .gitignore created successfully")
                            else:
                                print("Failed to create .gitignore file")

                else:
                    if make_template(base_dir=full_path, template=template, fill=fill):
                        print(f"Template '{temp}' applied successfully to: {full_path}")
                    else:
                        print(f"Failed to apply template '{temp}'")
                    return

    # No template specified - use crt_files command
    else:
        if not oth:
            print("Missing arguments!")
            print("Use --help for usage information")
            print("\nExamples:")
            print("  crt -t my_template                    # Apply existing template")
            print("  crt -t my_template --append           # Create template from current dir")
            print("  crt -t my_template --remove           # Delete template")
            print("  crt . py                              # Process files in current directory")
            print("  crt --help                            # Show full help")
        else:
            crt_files(ext, oth)


if __name__ == "__main__":
    main()
