{%  macro get_vendor_names(VendorID) -%}

case
    when {{VendorID}} = 1 then 'Creatview Moblie Technologies, LLC'
    when {{VendorID}} = 2 then 'Verifone Inc.'
    when {{VendorID}} = 4 then 'Unknown Vendor'
end

{%- endmacro %}
