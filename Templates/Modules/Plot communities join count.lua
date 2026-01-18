local p = {}

function p.drawGraph()
	-- A series of (x,y) data points to graph
	local points = { "0, 1", "1, 4.5", "3, 2", "5, 4" }

	local pathElm = mw.html.create( 'polyline' )
		:css( 'stroke', 'red' )
		:attr( 'points', table.concat( points, ' ' ) )
		:attr( 'fill', 'none')
		:attr( 'stroke-width', "0.05px")
		-- Circle each point
		:css( 'marker', 'url(#circle)' )

	local axis = mw.html.create( 'path' )
		:css( 'stroke', 'black' )
		-- M means move to point, L means draw line from current point to specified point
		:attr( 'd', 'M 5 -0.1 L -0.1 -0.1 L -0.1 5' )
		:css( 'stroke-width', "0.2px")
		:css( 'stroke-linecap', 'square' )
		:css( 'fill', 'none' )

	-- Circle marker for each data point
	local marker = mw.html.create( 'marker' )
		:attr( 'id', 'circle' )
		:attr( 'markerWidth', '10' )
		:attr( 'markerHeight', '10')
		:attr( 'refX', '5' )
		:attr( 'refY', '5' )
		:tag( 'circle' )
			:attr( { cx = 5, cy = 5, r = 4, stroke = "red", fill = "none" } )
		:done() 

	return mw.svg.new()
		:setImgAttribute( 'width', '200' )
		:setAttribute( 'viewBox', "-0.5 -0.5 6, 6" )
		-- Make origin be bottom left
		:setAttribute( 'transform', 'scale(1,-1)')
		:setContent( tostring(axis) .. tostring(marker) .. tostring(pathElm) )
		:toImage()
end

return p