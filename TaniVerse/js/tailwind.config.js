tailwind.config = {
    theme: {
        extend: {
            fontFamily: {
                'poppins': ['"Poppins"'],
            },
            colors: {
                'primary': '#1A5319',
                'second': '#508D4E',
                'additional1': '#80AF81',
                'additional2' : '#D6EFD8'
            }
        }
    },
    variants: {
        extend: {
            visibility: ["group-hover"],
        },
    },
}