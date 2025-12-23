# Voice Package (Echovoice)

This directory is a placeholder for the echovoice voice client package.

## Importing Echovoice from Local Path

To import the echovoice code from your local development environment:

### Step 1: Copy the Local Echovoice Folder

From the repository root, run:

```bash
cp -r /home/jacob/Desktop/echovoice/* packages/voice/
```

This will copy all files from your local echovoice directory into this package.

### Step 2: Verify the Import

Check that the files were copied successfully:

```bash
ls -la packages/voice/
```

You should see all your echovoice source files.

### Step 3: Commit the Changes

Stage and commit the imported files:

```bash
git add packages/voice/
git commit -m "feat: Import echovoice package from local development"
```

### Step 4: Push and Create PR

Push your changes and create a pull request for review:

```bash
git push origin <your-branch-name>
```

Then create a PR on GitHub for the team to review the echovoice integration.

## Next Steps After Import

Once echovoice is imported:

1. Review and update the package.json if it exists
2. Ensure dependencies are properly declared
3. Add any necessary build scripts
4. Update documentation specific to the voice package
5. Add tests if not already present

## Integration with Monorepo

This package will be part of the Goeckoh monorepo workspace. Dependencies can be managed at the workspace level or package level as needed.
