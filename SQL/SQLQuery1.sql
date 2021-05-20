USE [EOL_RESULTS]
GO

/****** Object:  Table [dbo].[EOL_BAU_]    Script Date: 19/05/2021 15:04:27 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[EOL_BAU](
	[Column1] [int] NULL,
	[name] [nvarchar](1500) NULL,
	[result] [nvarchar](1500) NULL,
	[value] [nvarchar](1500) NULL,
	[expectedvalue] [nvarchar](1500) NULL,
	[status] [nvarchar](1500) NULL,
	[lowerlimit] [nvarchar](1500) NULL,
	[upperlimit] [nvarchar](1500) NULL,
	[lowerwarning] [nvarchar](1500) NULL,
	[upperWarning] [nvarchar](1500) NULL,
	[units] [nvarchar](1500) NULL,
	[runtime] [nvarchar](1500) NULL,
	[cycles] [int] NULL,
	[timestamp] [datetime] NULL,
	[details] [nvarchar](4000) NULL,
	[Index] [nvarchar](1500) NULL
) ON [PRIMARY]
GO


