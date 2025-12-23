# packages/voice - EchoVoice Package

This directory is the placeholder for the **echovoice** local codebase.

## Import Instructions

To import your local echovoice code into this package:

1. **Copy the local echovoice directory into this package:**
   ```bash
   cp -r /home/jacob/Desktop/echovoice/* /path/to/goeckoh/packages/voice/
   ```

2. **Verify the files are copied:**
   ```bash
   ls -la packages/voice/
   ```

3. **Stage and commit the files:**
   ```bash
   git add packages/voice/
   git commit -m "Import echovoice codebase into packages/voice"
   ```

4. **Push the changes:**
   ```bash
   git push origin add-echovoice-scaffold
   ```

5. **Open a follow-up PR** to integrate the echovoice functionality with the rest of the monorepo.

## Next Steps

After importing echovoice:
- Review and update any package.json or dependencies
- Ensure build scripts are compatible with the monorepo structure
- Add integration points with other packages (backend, mobile-client, web-dashboard)
- Update documentation to reflect the new structure
