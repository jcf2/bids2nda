def verify_guid_file(filepath):
    """
    Verify GUID mapping file parsing
    
    Checks:
    1. File can be read
    2. Lines can be parsed as expected
    3. Provides details about the parsing
    """
    try:
        # Read the file contents
        with open(filepath, 'r') as f:
            file_contents = f.read()
        
        # Split into non-empty lines
        lines = [line.strip() for line in file_contents.split("\n") if line.strip()]
        
        print(f"Total non-empty lines: {len(lines)}")
        
        # Attempt parsing as in the original code
        try:
            # Parse lines, splitting on ' - '
            guid_mapping = dict([line.split(" - ") for line in lines])
            
            # Print parsing details
            print("\nParsing successful!")
            print(f"Number of entries: {len(guid_mapping)}")
            
            # Show first few entries
            print("\nFirst few entries:")
            for i, (key, value) in enumerate(list(guid_mapping.items())[:5]):
                print(f"{key} -> {value}")
            
            # Additional checks
            print("\nAdditional checks:")
            # Check for duplicate keys
            if len(guid_mapping) < len(lines):
                print("WARNING: Duplicate keys detected!")
            
            # Check key and value formats
            key_formats = set(type(k) for k in guid_mapping.keys())
            value_formats = set(type(v) for v in guid_mapping.values())
            print("Key types:", key_formats)
            print("Value types:", value_formats)
            
        except ValueError as parse_error:
            print("\nParsing failed!")
            print("Error details:", parse_error)
            
            # Provide more detailed error information
            print("\nSample lines:")
            for line in lines[:5]:
                print(f"Line: '{line}'")
                try:
                    parts = line.split(" - ")
                    print(f"  Splits into: {parts}")
                except Exception as e:
                    print(f"  Could not split: {e}")
    
    except Exception as read_error:
        print(f"Could not read file {filepath}")
        print("Error details:", read_error)

# Support running as a script
# Example usage: 
#    python verify_guid_file.py myids.txt
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        verify_guid_file(sys.argv[1])
        
