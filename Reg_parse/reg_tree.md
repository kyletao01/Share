- memoryMaps
  - memoryMap
    - name
    - **addressBlock**
      - name
      - range:  -> address_width
      - width:  -> data_width
      - baseAddress
      - parameters
      - description
      - vendorExtensions:
        - abbreName
        - rtlGeneration
          - busRegOut
          - wdataBP
          - UnitAddrDeepth
      - **register**
        - name
        - description
        - addressOffset
        - size:  default equal to  addressBlock.width
        - access: default is read-write  
        - vendorExtensions:
          - abbreName
        - **field**
          - name
          - description
          - bitOffset
          - bitWidth
          - resets
            - reset
              - value
              - mask
          - access:read-write(default), read-only, write-only, readwriteOnce,and writeOnce
          - modifiedWriteValue:  oneToClear,oneToToggle,oneToSet,zeroToClear, zeroToSet,zeroToToggle,clear,set , modify
          - readAction: clear, set, modify
          - vendorExtensions:
            - abbreName
            - rtlGeneration
              - rtlIOAccess
